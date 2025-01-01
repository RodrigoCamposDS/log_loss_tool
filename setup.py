from setuptools import setup, find_packages

setup(
    name="log_loss_tool",
    version="0.1.0",
    description="A Python tool to visualize the Log-Loss function.",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),  # Detecta automaticamente o pacote no subdiretório
    install_requires=[
        "numpy>=1.21.0",
        "matplotlib>=3.4.0",
    ],
    python_requires=">=3.6",
)