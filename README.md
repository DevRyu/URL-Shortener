# URL Shortener

## 프로젝트 설명
bit/ly처럼 
가변적 길이의 URL을 5자리 Base62 해시값으로 URL 길이를 줄여주는 API


### 사용가능한 api
```
short_link 생성  API
curl -d '{"url":"http://aaa3.caoasdaasddslaasdadkasasdddasdasdasdd"}' \
-H "Content-Type: application/json" \
-X POST http://localhost:5005/short-links

리다이렉션 API   
curl -X GET http://localhost:5005/r/00001
  
Short Link 목록 조회 API   
curl -X GET http://localhost:5005/short-links?size=50&page=1

Short Link 상세 조회 API   
curl -X GET http://localhost:5005/short-links/00001

기존에 생성된 Short Link의 Alias Name을 추가할 수 있는 API   
curl -d '{"aliasName":"alias_abc"}' \
-H "Content-Type: application/json" \
-X PATCH http://localhost:5005/short-links/00001
  
Alias Name이 포함된 Link를 통해 접속했을 때 원래 입력했던 URL로 redirect 해주는 API    
curl -X GET http://localhost:5005/a/alias_abc
  
기존에 생성된 Short Link를 삭제할 수 있는 API   
curl -X DELETE http://localhost:5005/short-links/00001
  
```

### 실행방법
```
docker-compose up
```
