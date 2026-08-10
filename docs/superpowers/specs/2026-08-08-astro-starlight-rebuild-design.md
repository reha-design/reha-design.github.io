# Astro Starlight 개발 학습노트 전환 설계

## 목표

`reha-design/reha-design.github.io`를 기존 Docusaurus 사이트에서 Astro Starlight 기반의 한국어 개발 학습노트로 전환한다. 최종 사이트는 `https://reha-design.github.io`에서 서비스하며, Markdown/MDX 문서와 Mermaid 다이어그램 및 정적 SVG 자료를 지속적으로 추가할 수 있어야 한다.

## 안전한 브랜치 전환

- 전환 직전의 Docusaurus 상태는 `backup/docusaurus-20260808` 브랜치에 보존한다.
- 저장소 기본 브랜치 이름은 `master`에서 `main`으로 실제 변경한다.
- 로컬 `main`은 `origin/main`을 추적한다.
- 새 GitHub Pages workflow는 `main` push와 수동 실행을 배포 진입점으로 사용한다.
- 기존 Docusaurus 문서와 블로그는 새 사이트로 옮기지 않고 백업 브랜치에서만 보존한다.

## 사이트 아키텍처

Astro를 정적 사이트 생성기로 사용하고 `@astrojs/starlight`를 문서 UI와 탐색 구조에 사용한다. `astro-mermaid`와 `mermaid`를 통해 Markdown의 `mermaid` 코드 블록을 빌드 시 렌더링한다. 사용자 GitHub Pages 저장소이므로 `site`만 `https://reha-design.github.io`로 지정하고 `base`는 설정하지 않는다.

Starlight는 루트 경로에 `ko-KR` 한국어 locale을 사용한다. 현재 Starlight에서 루트 단일 언어 사이트는 `defaultLocale: 'root'`와 `locales.root`로 설정하여 `/ko` 접두사나 깨진 홈 링크 없이 `https://reha-design.github.io/`에서 제공한다. 사이트 제목은 `레하의 개발 학습노트`, 설명은 `백엔드, CS, 네트워크, 보안, 데이터베이스, 인프라 학습 기록`으로 고정한다. 사이드바는 Network, Security, Database, Infra, Backend 순서이며 각 디렉터리에서 자동 생성한다.

## 파일 구조와 책임

- `astro.config.mjs`: Astro, Mermaid, Starlight, 사이트 URL, 한국어 locale 및 사이드바 설정
- `src/content.config.ts`: Starlight 문서 콘텐츠 컬렉션 등록
- `src/content/docs/index.mdx`: 사이트 소개, 학습 카테고리, 문서 운영 원칙
- `src/content/docs/network/tcp-udp-firewall-ips.md`: 첫 네트워크 학습 문서와 Mermaid 예제
- `src/content/docs/{security,database,infra,backend}/.gitkeep`: 아직 비어 있는 카테고리 구조 보존
- `public/diagrams/.gitkeep`: SVG 저장 경로 보존
- `.github/workflows/deploy.yml`: `main`에서 GitHub Pages 빌드·배포
- `README.md`: 목적, 기술 스택, 로컬 개발, 빌드, 배포, 문서 구조 안내
- `docs/superpowers/`: Docusaurus 콘텐츠와 분리된 전환 설계 및 구현 계획 보존

기존 `blog`, Docusaurus용 `docs` 콘텐츠, `src`, `static`, `.docusaurus`, `build`, `docusaurus.config.js`, `sidebars.js`, `bun.lock`과 기존 Node 패키지 파일은 제거한다. 단, 새로 작성한 `docs/superpowers`의 설계 및 계획 문서는 제거 대상에서 제외한다.

## 콘텐츠 설계

홈 문서는 학습 사이트의 목적과 다섯 개 카테고리를 소개하고, 모든 학습 문서가 한 줄 요약, 핵심 개념, 동작 방식, 실무 예시, 면접 답변, 꼬리 질문 흐름을 따르도록 안내한다.

첫 학습 문서는 TCP와 UDP를 전송 계층 프로토콜로, 방화벽과 IPS를 보안 시스템으로 구분한다. 비교 표, 전체 트래픽 흐름도, TCP 3-way handshake, 사용 사례, 보안 장비의 판단 기준 및 면접 답변을 포함한다. 흐름도와 시퀀스 다이어그램은 Mermaid로 작성한다.

설명용 구조도는 Mermaid를 기본으로 하고, 고정 이미지·로고·정교한 그림은 `public/diagrams/`의 SVG로 저장하여 `/diagrams/<파일명>.svg` 경로로 참조한다.

## 배포 흐름

`main`에 push되면 GitHub Actions가 저장소를 체크아웃하고 `withastro/action`으로 npm 의존성 설치, Astro 빌드, Pages 아티팩트 업로드를 수행한다. 배포 job은 빌드 성공 후 `actions/deploy-pages`로 `github-pages` 환경에 배포한다. workflow에는 `contents: read`, `pages: write`, `id-token: write` 권한과 중복 배포를 제어하는 concurrency 설정을 둔다.

## 오류 처리와 검증

- 의존성 설치 오류는 `npm install` 종료 코드와 로그로 확인한다.
- 구성, Markdown/MDX 또는 Mermaid 오류는 `npm run build`가 실패하도록 두고 원인을 수정한 뒤 전체 빌드를 다시 실행한다.
- 개발 서버를 실행해 홈, Network 사이드바, 첫 학습 문서 및 Mermaid 출력이 실제 HTML에서 제공되는지 확인한다.
- 빌드 산출물에서 Docusaurus 관련 문자열과 설정 잔재가 없는지 검사한다.
- push 후 GitHub Actions run이 성공했는지 확인하고 `https://reha-design.github.io`의 응답 및 주요 콘텐츠를 확인한다.

## 완료 조건

1. 원본 Docusaurus 상태가 원격 `backup/docusaurus-20260808`에 존재한다.
2. GitHub 기본 브랜치와 로컬 작업 브랜치가 `main`이다.
3. `npm run build`가 종료 코드 0으로 완료된다.
4. Starlight 한국어 문서 UI, Network 사이드바, TCP/UDP/방화벽/IPS 문서가 표시된다.
5. Mermaid 다이어그램이 렌더링된다.
6. `public/diagrams/`가 Git에서 유지된다.
7. `main` push 후 GitHub Pages 배포가 성공하고 공개 사이트가 응답한다.
