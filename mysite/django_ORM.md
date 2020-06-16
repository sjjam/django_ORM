# Django ORM
---
## CREATE
**1. INSERT INTO TABLE (column1, column2...) VALUES (values1, values2...)**
```python
# 첫번째 방법
article = Article()
article.title = 'first'
article.content = 'django!'
article.save()

# 두 번째 방법
# 어느 변수에 어떤 값을 넣을건지 명시
# id가 생략되어 있을 뿐, 자동으로 생성된다.
article = Article(title='second', content='django!')
article.save()

# 세 번째 방법
Article.objects.create(title='third', content='django!')
```
---
## READ
**2. SELECT * FROM articles_article**
```python
# 전체 조회
article = Article.objects.all()
```

**3. SELECT * FROM articles_article WHERE title='first'**
```python
# 특정 제목 불러오기
Article.objects.filter(title='first')
```

**SELECT * FROM articles_article WHERE title='first' LIMIT 1**
```python
Article.objects.filter(title='first').first()
Article.objects.filter(title='first').last()
Article.objects.filter(title='first')[0]
```

**SELECT * FROM articles_article WHERE id=1**
```python
Article.objects.get(id=1)
Article.objects.get(pk=1)
# 주의점
# 고유값이 아닌 내용을 필터링 해서
# 2개 이상의 값이 찾아지면 오류를 발생한다.
# 없는 것을 가지고 오려고 해도 오류 발생
```

**Like / startswith / endswith**
```python
# 특정 문자열을 포함 하고 있는가
Article.objects.filter(title__contains='fir')
# 특정 문자열로 시작 하는가
Article.objects.filter(title__startswith='SE')
# 특정 문자열로 끝나는가
Article.objects.filter(content__endswith='ha')
```
**ASC / DESC**
```python
Article.objects.all().order_by('pk')
Article.objcets.all().order_by('-pk')
Article.objects.all()[::-1]
```
---
## UPDATE
**UPDATE articles_article SET title='byebye' WHERE id=1**
```python
# 수정
article = Article.objects.get(pk=1)
article.title = 'byebye'
article.save()
```
---
## DELETE
**DELETE FROM articles_article WHERE id=1**

```python
# 삭제
article = Article.objects.get(pk=1)
article.delete()
```