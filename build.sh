IMAGE_TAG="latest"

# # Construir imagen para `test_database`
# cp docker/DockerfileTEST .
# IMAGE_NAME_DATABASE="test_database"
# docker build -t ${IMAGE_NAME_DATABASE}:${IMAGE_TAG} -f DockerfileTEST .
# rm DockerfileTEST



# Construir imagen para `nexus1-backend`
cp docker/Dockerfile .
IMAGE_NAME_BACKEND="nexus1-backend"
docker build -t ${IMAGE_NAME_BACKEND}:${IMAGE_TAG} -f Dockerfile .
rm Dockerfile




