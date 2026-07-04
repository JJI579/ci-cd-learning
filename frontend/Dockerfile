FROM oven/bun:latest as frontend
WORKDIR /frontend

# COPY package.json ./
# COPY bun.lock ./
# COPY src ./src
# COPY index.html ./
# COPY tsconfig.json ./
# COPY tsconfig.app.json ./
# COPY tsconfig.node.json ./

COPY . ./
RUN rm -rf node_modules
RUN bun install
RUN bun run build

# Now host with nginx

FROM nginx

COPY --from=frontend /frontend/dist/ /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf

CMD ["nginx", "-g", "daemon off;"]
