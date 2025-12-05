<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
</head>
<body>

<h1>📌 파이썬 알고리즘 문제풀이 채점기 (Mac 사용가능)</h1>

<p>이 프로그램은 <strong>김태원 강사님의 "파이썬 알고리즘 문제풀이 입문 (코딩테스트 대비)"</strong> 강의를 위한 채점 도구입니다.<br>
맥 사용자를 위해 직접 제작되었습니다.<br/>
  코딩테스트 환경과 최대한 비슷한 환경을 제공합니다. <br/>
  정답 채점은 test.py의 print() 내용을 통해 채점됩니다.<br/>
  추정 복잡도는 신뢰도가 낮습니다.
</p>

<p>강의 링크: 
<a href="https://www.inflearn.com/course/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8/dashboard" target="_blank">인프런 강의 바로가기</a>
</p>

<h2>🖼 채점 화면 예시</h2>
<img width="495" height="442" alt="image" src="https://github.com/user-attachments/assets/4cbe2a05-997c-4479-a9b4-876c106c79d1" />

<p>강의 문제 풀이를 <code>solution.py</code>에 작성하면, 이 프로그램이 자동으로 테스트하고 결과를 보여줍니다.</p>

<h2>📂 사용 방법</h2>
<ol>
<li>문제 폴더 안에 다음 두 파일을 위치시킵니다.</li>
<img src="https://github.com/user-attachments/assets/2a0f9678-e2e2-4e4b-a673-3f283885b527" alt="문제 폴더 구조" width="400"><br>
<ul>
<li><code>solution.py</code> → 문제 풀이 파일</li>
<li><code>test.py</code> → 채점기 파일</li>
</ul>
<li><code>solution.py</code>에 정답 코드를 작성합니다.</li>
<li><code>test.py</code>를 실행하여 자동 채점합니다.</li>
</ol>

<h2>⚙️ 옵션</h2>
<p><strong>test.py</strong> 상단의 설정으로 단계별 테스트 가능:</p>
<pre>
RUN_FLAG = 1      # 0 = 전체 테스트, 1 = 특정 테스트만 실행
TOTAL_TEST = 5    # 총 테스트 개수
</pre>

<p>디버깅 출력이 필요할 때:</p>
<pre>
print("DEBUG 메시지", file=sys.stderr)
</pre>

<h2>✅ 특징</h2>
<ul>
<li>Mac 환경 최적화</li>
<li>실행 시간, 메모리, 결과 비교 자동</li>
<li>디버깅용 출력 지원</li>
</ul>

<h2>🚨 알려진 문제점</h2>
섹션2-7.소수문제 out파일의 인코딩 UTF-8 변경 필요

</body>
</html>
