FROM oven/bun:latest
WORKDIR /frontend

COPY package.json ./
COPY bun.lockb ./
COPY src ./

RUN bun install

