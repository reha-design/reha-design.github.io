import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import mermaid from 'astro-mermaid';

export default defineConfig({
  site: 'https://reha-design.github.io',
  integrations: [
    mermaid({ autoTheme: true }),
    starlight({
      title: '레하의 개발 학습노트',
      description: '백엔드, CS, 네트워크, 보안, 데이터베이스, 인프라 학습 기록',
      defaultLocale: 'root',
      locales: {
        root: { label: '한국어', lang: 'ko-KR' },
      },
      social: [
        { icon: 'github', label: 'GitHub', href: 'https://github.com/reha-design' },
      ],
      sidebar: [
        { label: 'Network', items: [{ autogenerate: { directory: 'network' } }] },
        { label: 'Security', items: [{ autogenerate: { directory: 'security' } }] },
        { label: 'Database', items: [{ autogenerate: { directory: 'database' } }] },
        { label: 'Infra', items: [{ autogenerate: { directory: 'infra' } }] },
        { label: 'Backend', items: [{ autogenerate: { directory: 'backend' } }] },
      ],
    }),
  ],
});
