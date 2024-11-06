cp docker/Dockerfile .

IMAGE_NAME="nexus1-backend"
IMAGE_TAG="latest"

docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .


rm Dockerfile
