FROM python:3.7
WORKDIR /bq_test
RUN curl -sSL https://sdk.cloud.google.com | bash
ENV PATH $PATH:/root/google-cloud-sdk/bin
COPY requirements.txt .
RUN pip install -r requirements.txt
ENTRYPOINT ["bash"]