from invoke import run, task
import os


@task
def launch(ctx, resource_group='tldr', cluster_name='tldr-server', num_nodes=1, location='centralus'):
    run(f"az group create --name {resource_group} --location {location}")
    run(f"az aks create --resource-group {resource_group} --name {cluster_name} --node-count {num_nodes} --generate-ssh-keys", echo=True, hide=False)
    run(f"az aks get-credentials --resource-group {resource_group} --name {cluster_name}", echo=True, hide=False)
    run("helm init")
    run("kubectl rollout status -w deployment/tiller-deploy --namespace=kube-system") # wait for helm to install
    run('helm install stable/nginx-ingress', echo=True, hide=False)
    run('kubectl create -f app.yml')
    run('kubectl create -f api.yml')
    run('kubectl create -f ingress.yml')

@task
def delete(ctx, resource_group='tldr'):
    run(f"az group delete --name {resource_group} --yes", echo=True, hide=False)

@task
def deploy_conda(ctx):
    run(f"conda build conda.recipe --output-folder build-output", echo=True, hide=False)
    build_filename = os.path.basename(run(f"conda build conda.recipe --output", echo=True, hide=False).stdout.strip())
    run(f"conda convert build-output/osx-64/{build_filename} --platform linux-64 --output-dir build-output", echo=True, hide=False)
    run(f"anaconda upload build-output/osx-64/{build_filename} --interactive", echo=True, hide=False)
    run(f"anaconda upload build-output/linux-64/{build_filename} --interactive", echo=True, hide=False)

@task
def deploy_docker(ctx, docker_repo='pkell/tldr-server'):
    run(f"docker build . --tag {docker_repo}")
    run(f"docker push {docker_repo}:latest") # TODO: why is this being denied?

@task
def deploy(ctx, docker_repo='pkell'):
    deploy_conda(ctx)
    deploy_docker(ctx, docker_repo)
