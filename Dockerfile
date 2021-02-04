FROM centos:latest
MAINTAINER hitechinstitution
RUN yum -y install httpd
COPY index.html /var/www/html/
CMD [“/usr/sbin/httpd”, “-D”, “FOREGROUND”]
CMD ["systemctl start httpd”]
EXPOSE 80
