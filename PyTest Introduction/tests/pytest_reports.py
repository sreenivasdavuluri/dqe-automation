import subprocess

# Install pytest-html for HTML reports
subprocess.run(["pip", "install", "pytest-html"])

# Run pytest with HTML report generation
subprocess.run(["pytest", "--html=report.html"])
