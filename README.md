# 🚀 EC2 Real-Time Monitoring Tool

🔧 **Description**

This project is a **robust monitoring tool** developed with **Python, Flask, and Boto3** to track the **status of EC2 instances in real-time**.

✅ Leverages **Boto3** to interface with AWS EC2 API  <br />
✅ Fetches critical information: instance status, system status, and state  <br />
✅ Implements a **dynamic web interface** using Flask for intuitive monitoring   <br />

---

## 📂 Project Structure

```
project/
├── templates/              # HTML templates for Flask
├── .gitignore              # Git ignore file
├── ec2-status-check.py     # Main Flask application script
└── requirements.txt        # Project dependencies
```

---

## 💡 Features

✨ Real-time monitoring of EC2 instances  <br />
✨ Fetches instance status, system status, and state details   <br />
✨ Dynamic web interface with Flask   <br />
✨ Simple deployment on local machine or EC2 instance   <br />

---

## 🛠️ Technologies Used

* 🐍 **Python**
* 🌐 **Flask**
* ☁️ **Boto3**
* 💻 **AWS EC2**

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

### 2️⃣ Install requirements

It’s recommended to use a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Configure AWS Credentials

Ensure your AWS credentials are configured using:

```bash
aws configure
```

Or set environment variables:

```powershell
setx AWS_ACCESS_KEY_ID "your_access_key"
setx AWS_SECRET_ACCESS_KEY "your_secret_key"
setx AWS_DEFAULT_REGION "your_region"
```

### 4️⃣ Run the application

```bash
python ec2-status-check.py
```

Visit **[http://127.0.0.1:5000](http://127.0.0.1:5000)** in your browser to view the real-time EC2 status dashboard.

---

## ✅ Prerequisites

* AWS account with EC2 read permissions
* Python 3.6+ installed
* AWS CLI configured or environment variables set

---

## 📌 Notes

* Customize `ec2-status-check.py` for your instance filters or specific regions.
* Deploy on an EC2 instance or any server to monitor from anywhere.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request.

---

### ✨ Author

Ahmed Elshnawy
