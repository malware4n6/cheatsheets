FROM debian:bookworm-slim

WORKDIR /hiew

# Update package lists and install required packages
RUN apt update && \
    apt install -y wget software-properties-common gnupg2 winbind locales locales-all
ENV LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8 LANGUAGE=en_US.UTF-8

# Add Wine repository and install Wine
RUN dpkg --add-architecture i386 && \
    wget -nc https://dl.winehq.org/wine-builds/winehq.key && \
    apt-key add winehq.key && \
    add-apt-repository -y 'deb https://dl.winehq.org/wine-builds/debian/ bookworm main' && \
    apt update  && \
    apt install -y wine32:i386

# Cleanup unnecessary files
RUN apt clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV WINEDEBUG=fixme-all

COPY hiew /hiew
COPY bashrc /root/.bashrc
CMD ["bash"]
