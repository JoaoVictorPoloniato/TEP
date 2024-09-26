# Use uma imagem base oficial do Node.js
FROM node:14

# Defina o diretório de trabalho dentro do container
WORKDIR /usr/src/app

# Copie o arquivo package.json e package-lock.json (se existir)
COPY package*.json ./

# Instale as dependências do projeto
RUN npm install

# Copie o restante do código do projeto
COPY . .

# Exponha a porta que o aplicativo Node.js estará escutando
EXPOSE 3000

# Comando para rodar o aplicativo
CMD ["node", "src/index.js"]
