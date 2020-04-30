import os
import sys
import time
import subprocess
import click
import jinja2

logo = '''
 _   __   _   _____   _____       ___   _       _
| | |  \ | | /  ___/ |_   _|     /   | | |     | |
| | |   \| | | |___    | |      / /| | | |     | |
| | | |\   | \___  \   | |     / / | | | |     | |
| | | | \  |  ___| |   | |    / /  | | | |___  | |___
|_| |_|  \_| /_____/   |_|   /_/   |_| |_____| |_____|
                                   
					---by UIH POS
'''

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
CHARTS_PATH = os.path.join(BASE_PATH, 'charts') 

@click.command()
def install():
    """automate install product."""
    
    click.clear()
    click.secho(logo, fg="blue")
    click.secho("[+] Install start...", fg="cyan")
    click.secho("[+] Check environment start...", fg="cyan")
    
    if not env_check():
        click.secho("[+] environment check failed! please contact administrator", fg="red")
        click.pause()
        sys.exit(0)

    env_info = click.prompt(click.style("Please choose env information", fg="magenta"), type=click.Choice(["prod","preprod","dev"]), default="prod")
    
    tag_name = click.prompt(click.style("Please input tag name like R001.0.0.01-20200415", fg="magenta"), default="stable")

    config_ok = click.confirm(click.style("Configure file have existed or not ?", fg="magenta"), default=True, show_default=True)

    if not config_ok:
        click.secho("[+] This function is in development...", fg="red")
        #click.pause()
        #sys.exit(0)
        generate_config(env_info, tag_name)

    click.secho("[+] Installing %s environment..." % env_info, fg="cyan")

    helmInstallAuth(env_info, tag_name)

    click.secho("[+] Environment has been installed!", fg="green", bold=True)


def env_check(): 
    click.secho("   [+] Check helm command...", fg="cyan")
    
    find_result = False
    for cmd_path in os.environ.get('PATH').split(':'):
        if os.path.isdir(cmd_path) and "helm" in os.listdir(cmd_path):
            find_result = True
            break

    if not find_result:
        click.secho("   [+] Could not found helm installed!", fg="red", bold=True)
        return False

    click.secho("   [+] Clearing envirmont...", fg="cyan")
    uninstall_ret = helmUninstall()

    if not uninstall_ret:
        click.secho("   [+] Clear envirmont failed...", fg="red", bold=True)
        return False
    return True


def helmUninstall():
    result = True
    products = ['auth', 'chatbot', 'solar', 'library', 'imagecloud']
    with click.progressbar(products) as bar:
        #for product_name in ['auth', 'chatbot','solar', 'library', 'imagecloud']:
        for product_name in bar:
            uninstall_cmd = "helm delete %s --purge" % product_name
            proc = subprocess.Popen(uninstall_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
            proc.wait()
            stdout_ret = proc.stdout.read()
            stderr_ret = proc.stderr.read()

            if "not found" in stderr_ret or "deleted" in stdout_ret:
                click.secho("\n       [+] Clear %s release success..."%product_name, fg="green")
            else:
                click.secho("\n       [+] Clear %s release failed..."%product_name, fg="red")
                result = False
    return result
    

def helmInstallAuth(env_info, tag_name):

    status = True
    
    click.secho("   [+] Install Auth package ...", fg="cyan")

    chart_path = os.path.join(CHARTS_PATH, 'auth')  
    os.chdir(chart_path)

    install_cmd = "helm install -f values-{0}.yaml  --set server.image.tag={1} --set uap.image.tag={1} --set uapWeb.image.tag={1} --set wechatWeb.image.tag={1} --namespace {0} --name auth ./".format(env_info, tag_name)

    #print(install_cmd)
    proc = subprocess.Popen(install_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
    proc.wait()
    stdout_ret = proc.stdout.readlines()
    stderr_ret = proc.stderr.read()

    if "DEPLOYED" in stdout_ret[3]:
        click.secho("   [+] Install Auth package success...", fg="green")
    else:
        click.secho("   [+] Install Auth package failed...", fg="red")
    
    return status



def generate_config(env_info, tag_name):
    
    default_conf = {
        "mysql_host":"",
    }

    default_conf["mysql_host"] = click.prompt(click.style("Mysql host", fg="magenta"), default=default_conf.get("mysql_host"))
    
    click.secho("[+] Start to generate value file...", fg="cyan")

    values_dir = os.path.join(CHARTS_PATH, "auth")
    TemplateLoader = jinja2.FileSystemLoader(values_dir)
    TemplateEnv = jinja2.Environment(loader=TemplateLoader)
    config_template = TemplateEnv.get_template('values.yaml.j2')

    value_filename = "values-%s.yaml"%env_info
    value_filepath = os.path.join(values_dir, value_filename)
    with open(value_filepath, "wb") as cfg_file:
        cfg_file.write(config_template.render(**default_conf).encode("utf-8"))
        click.secho("   [+] Generate Auth value file  success...", fg="green")

if __name__ == '__main__':
    install()

