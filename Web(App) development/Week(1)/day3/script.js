// --- 1. 기본 클릭 이벤트 (알림창) ---
const testBtn = document.getElementById('test-btn');
if (testBtn) {
    testBtn.addEventListener('click', () => {
        alert('팝업창 클릭 이벤트가 잘 작동합니다!');
    });
}

// --- 2. 다크모드 제어 ---
const themeBtn = document.getElementById('theme-toggle');
const body = document.body;

if (themeBtn) {
    themeBtn.addEventListener('click', () => {
        // body 태그에 dark-mode 클래스를 넣었다 뺐다 함
        body.classList.toggle('dark-mode');
        
        // 아이콘 변경
        if (body.classList.contains('dark-mode')) {
            themeBtn.textContent = '라이트모드';
        } else {
            themeBtn.textContent = '다크모드';
        }
    });
}

// --- 3. 모바일 메뉴 제어 ---
const menuBtn = document.getElementById('mobile-menu');
const navList = document.getElementById('nav-list');

if (menuBtn && navList) {
    menuBtn.addEventListener('click', () => {
        navList.classList.toggle('active');
    });
}

// --- 4. 비동기 API 통신 (여우 이미지 가져오기) ---
const fetchBtn = document.getElementById('fetch-btn');
const foxImg = document.getElementById('fox-image');

// async 키워드로 비동기 함수 선언
async function getRandomFox() {
    try {
        // 데이터 가져오기 전 로딩 상태 처리
        fetchBtn.disabled = true;
        fetchBtn.textContent = '가져오는 중...';

        // API 서버에 데이터 요청하고 기다림 (await)
        const response = await fetch('https://randomfox.ca/floof/');
        
        // 응답을 JSON 형태로 변환하고 기다림 (await)
        const data = await response.json();

        // 가져온 이미지 URL을 화면에 적용
        foxImg.src = data.image;
        foxImg.style.display = 'block';

    } catch (error) {
        alert('이미지를 가져오는데 실패했습니다. 인터넷 연결을 확인해주세요.');
        console.error('API 에러:', error);
    } finally {
        // 작업이 끝나면 버튼 상태 원상복구
        fetchBtn.disabled = false;
        fetchBtn.textContent = '귀여운 새로운 🦊 가져오기';
    }
}

// 버튼을 클릭했을 때 여우 사진 가져오는 함수 실행
if (fetchBtn) {
    fetchBtn.addEventListener('click', getRandomFox);
}

// 스크립트가 로드되자마자 여우 사진 한 장 먼저 가져오기
getRandomFox();