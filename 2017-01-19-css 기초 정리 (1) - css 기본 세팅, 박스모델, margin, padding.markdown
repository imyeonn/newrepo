---
title: "css 기초 정리 (1) - css 기본 세팅, 박스모델, margin, padding"
layout: post
date: 2017-01-19 10:02
image: /assets/images/post/001/17_00title.png
headerImage: true
tag:
- css
- css 기초
- 생활코딩
blog: true
author: Hyeyeon
description: css 기초 정리
---

### Summary:

[생활코딩 웹 기본수업](https://opentutorials.org/course/1688/9350) 중 css에 대해 기억해야 할 내용입니다.

---



## 기본 세팅

css는 항상 html과 함께 간다. css는 html을 예쁘게 하기 위해 존재한다. html은 **정보** 에 집중! css는 **시각적** 측면에 집중!

`<head>` 안 `<style>` 태그 안에 css가 들어간다. 따라서 이 안은 css문법에 따라 작성한다.

{% highlight html %}
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <style>

    /*css코드*/
    h1 {color:red}

    </style>
    <title></title>
  </head>
  <body>

  </body>
</html>
{% endhighlight %}

#### h1 {color:red}

* `h1` : 선택자(selector). html 내 태그 이름이자 css 코드의 주어 역할.
* `{color:red}` : 서술(description). 선택자에 어떤 효과를 줄지 서술함. 동사 역할.

---

## <style>에 속성 넣어보기

h1, h2, h3, h4에 각각의 속성을 넣어봤다.

* `;` : 속성과 속성을 구분할 때 사용
* `h3, h4` : 에 같은 속성을 동시에 적용하고 싶을 때 ,로 묶음
* `h4 {}` : h4에만 다른 속성을 추가하거나 제거할 때 따로 { } 추가

{% highlight html %}
<style>
  h1 {color: #427fed}
  h2 {
    text-decoration: underline;
    font-size: 10px
  }
  h3, h4 {
    color: #fff;
    background-color: #db4437
  }
  h4 {
    text-decoration: underline
  }
</style>
{% endhighlight %}

![pic1](/assets/images/post/001/17_01.png)
<figcaption class="caption">적용 결과</figcaption>

<br>

---

## 태그가 여러겹일 때

`<body>`를 보면 `h1`이 하나는 <header> 안에, 하나는 <header> 밖에 있다. 이 둘을 구분시키는 속성을 적용시켜보자.

* `header h1 { }` : 뒤따르는 태그를 띄어쓰기로 구분하고 나열한다.

{% highlight html %}
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <style>
      h1 {color: #333}
      header h1 {
        border: 1px solid #db4437;
        color: #db4437
      }
    </style>
    <title></title>
  </head>
  <body>
    <header>
      <h1>헤더 안 h1입니다.</h1>
    </header>
    <h1>헤더 밖 h1입니다.</h1>
  </body>
</html>
{% endhighlight %}

![pic2](/assets/images/post/001/17_02.png)
<figcaption class="caption">적용 결과</figcaption>

<br>

---

## css 박스모델

### 1. 각 리스트에 빨간색 점선 박스를 씌우고 싶다.

{% highlight html %}
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <style>
      li {
        border: 1px dotted #db4437;
        margin-bottom: 20px
      }
    </style>
    <title></title>
  </head>
  <body>
    <ul>
      <li>list1</li>
      <li>list2</li>
      <li>list3</li>
    </ul>

  </body>
</html>
{% endhighlight %}

![pic3](/assets/images/post/001/17_03.png)

### 2. list2에만 검정색 실선 박스을 채우고 싶다.

list2의 `<li>`에 `id="selected"`를 추가하고, 위 <style>에서는 `#selected { }`를 추가하고 그 안에 원하는 속성값을 넣는다.

* `#`과 `id`는 특수기호다. 맘대로 바꿔쓰면 안 된다. `#`은 id를 뜻한다.
* 물론 `id="selected"`에서 "selected"는 내 맘대로 바꿔도 된다.
* <style>에서 `selected { }` 을 하는게 아니다. 이렇게 되면 컴퓨터는 selected라는 태그를 찾는다. 내가 원하는 건 id가 "selected"인 <li> 태그에 검정색 실선 박스를 채우는 것이다.
* 추가적으로 검정색 실선 박스 외 margin을 줬다. 다른 리스트들을 margin이 좌, 우, 위 모두 0이고 아래만 20px이지만 list2의 margin은 좌, 우, 위, 아래 모두 40px이다.

{% highlight html %}
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <style>
      li {
        border: 1px dotted #db4437;
        margin-bottom: 20px
      }
      #selected {
        border: 1px solid #000;
        margin: 40px
      }
    </style>
    <title></title>
  </head>
  <body>
    <ul>
      <li>list1</li>
      <li id="selected">list2</li>
      <li>list3</li>
    </ul>

  </body>
</html>
{% endhighlight %}

![pic4](/assets/images/post/001/17_04.png)

<br>

### 3. 글자와 블럭 사이 간격이 좁은 것 같다. 늘리자.

padding 속성을 이용한다.

{% highlight html %}
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <style>
      li {
        border: 2px dotted #db4437;
        margin-bottom: 20px;
        padding: 30px
      }
    </style>
    <title></title>
  </head>
  <body>
    <ul>
      <li>list1</li>
      <li>list2</li>
      <li>list3</li>
    </ul>

  </body>
</html>
{% endhighlight %}

![pic5](/assets/images/post/001/17_05.png)

<br>

---

## float

### css로 이미지 편집하기

단순히 <body>에 그림과 글을 쓰면 아래 결과와 같이 그림이 너무 작거나 클 수 있다.

{% highlight html %}
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <img src="https://imyeonn.github.io/assets/images/post/001/09_04.png" />
    merchandising 즉, 상품화(상품기획)이 중요하다고 한다. 브랜드들을 많이 입점시키는 것이 경쟁력이 아니라 상품을 어떻게 고객에게 매력적으로 표현할 수 있는지가 핵심이다. 문제는 그 상품기획과 더불어 고객에게 특별한 경험을 제공함과 동시에 수익까지 내야 한다는 것이다.
  </body>
</html>
{% endhighlight %}

![pic6](/assets/images/post/001/17_06.png)
<figcaption class="caption">그림이 너무 커서 오른쪽이 짤렸다.</figcaption>

<br>

`float`를 이용하면 이미지를 왼쪽 혹은 오른쪽으로 옮기고 그 빈공간에 글자를 채울 수 있다.

* `float: left;` : 그림 왼쪽 정렬
*  `float: right;` : 그림 오른쪽 정렬

{% highlight html %}
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <style>
      img {
        width: 200px;
        float: left; /*또는 float: right;*/
      }
    </style>
    <title></title>
  </head>
  <body>
    <img src="https://imyeonn.github.io/assets/images/post/001/09_04.png" />
    merchandising 즉, 상품화(상품기획)이 중요하다고 한다. 브랜드들을 많이 입점시키는 것이 경쟁력이 아니라 상품을 어떻게 고객에게 매력적으로 표현할 수 있는지가 핵심이다. 문제는 그 상품기획과 더불어 고객에게 특별한 경험을 제공함과 동시에 수익까지 내야 한다는 것이다.
  </body>
</html>
{% endhighlight %}

![pic7](/assets/images/post/001/17_07.png)
<figcaption class="caption">float: left;</figcaption>

![pic8](/assets/images/post/001/17_08.png)
<figcaption class="caption">float: right;</figcaption>

---

이어지는 내용은 [css 기초정리 (2)](https://imyeonn.github.io/)에서 정리한다.

---
