# ES6 Basics

## Install Node

## Update your system to ensure it's up-to-date
```
sudo apt update
sudo apt upgrade
```

## Install NVM (Node Version Manager)
```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
```

* Close and reopen the terminal to apply configuration changes.
* This step is important for NVM to work properly.

## Install the latest stable version of Node.js using NVM
```
nvm install node
```

## Verify the installation of Node.js and npm
```
node -v
v20.6.1
npm -v
9.8.1
```

## Install Jest, Babel, and ESLint
Install Jest using:
```
npm install --save-dev jest
```
Install Babel using:
```
npm install --save-dev babel-jest @babel/core @babel/preset-env
```
Install ESLint using:
```
npm install --save-dev eslint
```

example "package.json":
```
{
  "type": "module",
  "scripts": {
    "dev": "node",
    "test": "jest",
    "lint": "./node_modules/.bin/eslint"
  },
  "devDependencies": {
    "@babel/core": "^7.22.17",
    "@babel/preset-env": "^7.22.15",
    "babel-jest": "^29.6.4",
    "eslint": "^8.49.0",
    "eslint-plugin-react": "^7.33.2",
    "jest": "^29.6.4"
  }
}
```

run:
```
npm run dev 0-main.js
npm run dev 1-main.js
npm run dev 2-main.js
npm run dev 3-main.js
npm run dev 4-main.js
npm run dev 5-main.js 
npm run dev 6-main.js 
npm run dev 7-main.js
npm run dev 8-main.js 
npm run dev 9-main.js
npm run dev 10-main.js 
npm run dev 11-main.js
npm run dev 12-main.js 
```