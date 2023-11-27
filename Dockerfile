FROM ubuntu
RUN apt-get update
RUN apt-get install -y nginx vim curl git python3 pip 
RUN pip3 install matplotlib flask numpy app xmlrunner
RUN git clone https://github.com/mohamad0880218/workflow.git 
#COPY .  ./
#CMD ["echo","Image Created"]
RUN pytest test_app.py --junitxml=report.xml
CMD ["python3","main.py"]
