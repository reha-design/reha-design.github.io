# 레하의 개발 학습노트

백엔드 개발자 취업 준비를 위해 CS, 네트워크, 보안, 데이터베이스, 인프라 개념을 정리하는 Astro Starlight 기반 문서 사이트입니다.

## Site

https://reha-design.github.io

## Stack

- Astro
- Starlight
- Markdown / MDX
- Mermaid
- GitHub Pages
- GitHub Actions

## Local Development

```bash
npm install
npm run dev
```

## Build

```bash
npm run build
```

## Deploy

`main` 브랜치에 push하면 GitHub Actions를 통해 GitHub Pages에 자동 배포됩니다.

## Structure

```text
src/content/docs/
  network/
  security/
  database/
  infra/
  backend/

public/diagrams/
```
