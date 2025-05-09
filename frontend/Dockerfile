FROM node:20-alpine

# 1. Set working directory
WORKDIR /app

# 2. Install Node deps
COPY package.json package-lock.json ./
RUN npm install

# 3  Copy everything else (excluding files in .dockerignore)
COPY . .


# 3.5 Build for production
RUN npm run build


# 4. Expose the port your dev/start script uses
EXPOSE 3000

# 5. Start the React development server
CMD ["npm", "run", "start"]
