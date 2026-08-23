FROM alpine:latest

RUN echo "Terraform infrastructure project" > /project-info.txt

CMD ["cat", "/project-info.txt"]
