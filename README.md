# k8s-cli
# CLI for IntelliSense.io

## How to use
### Installing the environment
- Requirements 
    - Python 
    - pip 

- Setup

    - ``` pip install pipenv```

    - ``` pipenv install ```

    - ``` pipenv shell ```

Once we have created the virtual environment and logged in, we can start testing the cli.

### How to use it 

To invoque te cli you should run the following comand

``` python -m k8s```

This will show you the cli options

```
Usage: python -m k8s [OPTIONS] COMMAND [ARGS]...

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  show

```

To check comand flags and calls you can run 

``` python -m k8s show --help```

```
Usage: python -m k8s show [OPTIONS]

Options:
  -S                Short the results by time descending
  --namespace TEXT  Define the namespace to get the tables values
  --help            Show this message and exit.

```

**It's required to have a local kubeconfig file before start to use the CLI.**

