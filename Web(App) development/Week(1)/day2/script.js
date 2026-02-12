// 1. 요소 선택 (HTML에서 ID나 클래스로 요소를 찾아 변수에 담습니다)
const themeToggleBtn = document.getElementById('theme-toggle');
const body = document.body;
const menuToggleBtn = document.getElementById('mobile-menu');
const navLinks = document.querySelector('.nav-links');

// 2. 다크 모드 기능
themeToggleBtn.addEventListener('click', () => {
    // body 태그에 'dark-mode' 클래스를 줬다 뺐다(toggle) 합니다.
    body.classList.toggle('dark-mode');

    // 버튼 아이콘 변경 (달 <-> 해)
    if (body.classList.contains('dark-mode')) {
        themeToggleBtn.textContent = '밝은모드';
    } else {
        themeToggleBtn.textContent = '다크모드';
    }
});

// 3. 모바일 메뉴 토글 기능
menuToggleBtn.addEventListener('click', () => {
    // 메뉴 리스트에 'active' 클래스를 토글해서 보이게/숨기게 합니다.
    navLinks.classList.toggle('active');
});