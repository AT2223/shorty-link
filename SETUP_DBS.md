# Cách setup database (mongodb)

## Mỗi thành viên sẽ tự setup database riêng trên máy
## Không được commit file .env lên github 

---

## 1. Cách cài đặt mongodb

### a. MacOS
```bash
brew tap mongodb/brew
brew install mongodb-community
brew services start mongodb-community
```

### b. Win
```bash
1. Tải https://www.mongodb.com/try/download/community
2. Chọn Install MongoDB 
3. Sau đó mở MongoDB compass
```

### c. Linux
```bash
sudo apt-get install -y mongodb
sudo service mongodb start
```

**Chạy thử 'mongo --version' để check thử coi cài chưa**

---

## 2. Tạo file .env
Tạo file .env trong mục backend
```bash
MONGODB_URL=mongodb://localhost:27017
DB_NAME=shorty_db
COLLECTION_NAME=links
```

## 3. Kiểm tra db chạy chưa
Vào MongoDB Compass rồi connect
```aiignore
mongodb://localhost:27017
```

## 4. Chạy backend
```bash
cd backend
uvicorn app.main:app --reload
```

Rồi test api ở đây nha
```aiignore
http://localhost:8000/docs
```