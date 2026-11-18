# Contexte principal : ./frontend
# Contexte nommé "nginx-conf" : ./devops/nginx (voir docker-compose.yml)

# Build du front
FROM node:22-alpine AS build

WORKDIR /app

# Dépendances d'abord (cache Docker : ne se réinstalle que si ces fichiers changent)
COPY package.json package-lock.json ./
RUN npm ci

# Code + build (tsc -b && vite build -> /app/dist)
COPY . .
RUN npm run build

# ---------- Étape 2 : nginx (non-root, écoute sur 8080) ----------
FROM nginxinc/nginx-unprivileged:1.27-alpine

COPY --from=nginx-conf nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 8080
