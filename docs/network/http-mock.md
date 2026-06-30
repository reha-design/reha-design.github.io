---
id: http-mock
title: HTTP 흐름 테스트 (Mermaid)
sidebar_position: 1
---

# HTTP 테스트용 문서

Docusaurus 지식베이스(Docs) 동작 및 Mermaid 다이어그램 렌더링 확인용.

## 전체 흐름

```mermaid
sequenceDiagram
    participant Browser
    participant Server

    Browser->>Server: HTTP Request
    Server-->>Browser: HTTP Response
```

## 확인 항목
- [x] 사이드바 메뉴 정상 출력
- [x] Mermaid 다이어그램 이미지화
