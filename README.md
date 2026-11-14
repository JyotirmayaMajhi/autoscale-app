#Auto-Scaling Web App on AWS
## What is this project?
   I built a small Python Flask app and deployed it on an AWS EC2 instance (Amazon Linux).The goal is to make it auto-scale:
   when CPU usage gets high, AWS should automatically add more servers.

## Endpoints
| Path | What it does |
|------|--------------|
| `/` | Shows a welcome message: "Hello from my auto-scaling app!" |
| `/health` | Returns `{"status": "ok"}`. Later, the load balancer will use it to check if the server is working. |
| `/load` | Keeps the CPU busy for 5 seconds. Later, this will be used to test auto scaling. |

## How to run it?
### 1. Launch an EC2 instance
- Amazon Linux 2023, t2.micro / t3.micro (free tier)
- Security group inbound rules:
  - SSH (port 22) from My IP
  - Custom TCP (port 5000) from My IP

### 2. Install Python tools and Git
```bash
sudo dnf install -y python3-pip git
```

### 3. Download the code
```bash
git clone https://github.com/YOUR-USERNAME/autoscale-app.git
cd autoscale-app
```

### 4. Create a virtual environment and install packages
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 5. Run the app
```bash
python3 app.py
```

### 6. Open it in a browser
`http://<EC2-public-IPv4>:5000/`

## What I learned
**Learned:** Python virtual environments, Git basics (init, add, commit, push) and connecting to GitHub with SSH keys.

##Problems I fixed
**Stuck package install:** `dnf` kept showing "Waiting for process with pid 2594
  to finish". I used `ps -p 2594 -o pid,cmd` to see that an earlier
`dnf install` (run without `-y`) was stuck waiting for a yes/no answer. I stopped it with `sudo kill -9 2594` and
 reran the install with `-y` so it couldn't get stuck again
