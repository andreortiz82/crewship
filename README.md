# Crewship

This project is an example of using CrewAI.

## Get started

Clone the project:

```
gh repo clone andreortiz82/crewship
cd crewship/

```

**Python Environment**

To kick off my Python virtual enviroment. I use the following commands:

- Instantiate the ENV for the first time, run: `python3 -m venv ./v`
- Activiate the ENV with `source v/bin/activate`. This will allow you to install your python dependencies in the `./v` directory to avoid any risk of version conflicts.
- Deactivate the virtual ENV with `deactivate`

I like to create aliases for myself:

```bash
alias vpk='deactivate'

function vpi() {
  python3 -m venv ./$1
  source $1/bin/activate
}

function vpa() {
  source $1/bin/activate
}
```

**Install**

Install the dependencies with `pip install crewai crewai-tools openai`

**Run**

Run the project with: `python3 main.py`
