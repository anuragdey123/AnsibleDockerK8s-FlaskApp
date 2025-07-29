# 🚀 Flask App Deployment using Ansible, Docker & Kubernetes

This project demonstrates how to **build**, **containerize**, and **deploy** a simple Flask web application on a Kubernetes cluster using **Ansible automation** and **Docker**.

> 🎯 Goal: One-click automated deployment from local machine to a running Kubernetes environment.

---

## 📸 Final Output

> 🌐 `http://localhost:5000`

Welcome to My Flask App — Deployed on Kubernetes using Ansible & Docker by Anurag 🚀

---

## 🧠 Tech Stack

- ⚙️ **Ansible** – for automation & orchestration
- 🐳 **Docker** – to containerize the app
- ☸️ **Kubernetes** – to manage deployment
- 🐍 **Python Flask** – lightweight backend framework
- 💻 **WSL + PowerShell** – development environment

---

## 📁 Project Structure

AnsibleDockerK8sProject3/
├── app/                   # Flask application
│   ├── app.py             # Main Python app
│   ├── Dockerfile         # Docker build file
│   └── requirements.txt   # Flask dependencies
│
├── k8s/                   # Kubernetes YAML files
│   ├── deployment.yaml
│   └── service.yaml
│
├── ansible/               # Ansible automation
│   ├── inventory
│   └── playbook.yml
🔧 Setup Instructions
1️⃣ Install Required Ansible Collections
ansible-galaxy collection install community.docker
ansible-galaxy collection install kubernetes.core
2️⃣ Run the Playbook
ansible-playbook ansible/playbook.yml -i ansible/inventory
3️⃣ Access Your App
Visit: http://localhost:5000
✨ Features
✅ Flask app runs inside Docker

✅ Kubernetes handles deployment & service exposure

✅ Ansible automates entire workflow

✅ Port 30080 mapped using NodePort service

✅ Fully working from scratch in WSL or Windows PowerShell



👤 Author
Anurag Dey
📍 DevOps Enthusiast | Python + Docker + K8s + GitOps
🔗 GitHub Profile

📢 Want to See This Live?
🚀 This is ready for cloud (like AWS EKS or DigitalOcean K8s). Just swap local cluster config and redeploy.

🙌 Acknowledgements
Big thanks to:

LinuxWorld Informatics Pvt. Ltd. 🙏

Open-source communities behind Ansible, Docker & Kubernetes






