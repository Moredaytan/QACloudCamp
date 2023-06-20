FROM python:3.8-alpine
WORKDIR ./user/test
COPY . .
RUN apk update && apk upgrade && apk add bash
RUN pip3 install -r requirement.txt
RUN pip3 install pytest
RUN pip3 install requests
RUN python -m venv myenv

CMD ["pytest", "tests"]