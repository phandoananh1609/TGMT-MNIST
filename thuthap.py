from sklearn.datasets import fetch_openml

# Tải dữ liệu MNIST
mnist = fetch_openml('mnist_784', version=1)

# Tải dữ liệu Fashion MNIST
fashion_mnist = fetch_openml('Fashion-MNIST', version=1)
