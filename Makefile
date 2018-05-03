DOCKER_IMAGE_NAME = python-gameoflife

.PHONY: build run_cpu run_gpu

build:
	docker build -t ${DOCKER_IMAGE_NAME} .

run_cpu:
	docker run --rm -it \
		--net host \
		-e DISPLAY=${DISPLAY} \
		-v ${HOME}/.Xauthority:/root/.Xauthority \
		-v ${PWD}:/app \
		${DOCKER_IMAGE_NAME} python cpu.py

run_gpu:
	docker run --rm -it \
		--runtime=nvidia \
		--net host \
		-e DISPLAY=${DISPLAY} \
		-v ${HOME}/.Xauthority:/root/.Xauthority \
		-v ${PWD}:/app \
		${DOCKER_IMAGE_NAME} python gpu.py
