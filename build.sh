cp docker/Dockerfile .

IMAGE_NAME="fast-api-example"
IMAGE_TAG="latest"

docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .


rm Dockerfile
