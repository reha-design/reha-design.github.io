import assert from 'node:assert/strict';
import { existsSync, readFileSync, rmSync } from 'node:fs';
import { join } from 'node:path';
import { spawnSync } from 'node:child_process';
import test from 'node:test';

const dist = join(process.cwd(), 'dist');
rmSync(dist, { recursive: true, force: true });

const build = spawnSync('npm run build', {
  cwd: process.cwd(),
  encoding: 'utf8',
  shell: true,
});

assert.equal(build.status, 0, `${build.stdout}\n${build.stderr}`);

test('builds the Korean Starlight home at /', () => {
  const homePath = join(dist, 'index.html');
  assert.equal(existsSync(homePath), true, 'dist/index.html must exist');
  const html = readFileSync(homePath, 'utf8');
  assert.match(html, /<html[^>]+lang="ko-KR"/);
  assert.match(html, /레하의 개발 학습노트/);
  assert.match(html, /Network/);
  assert.match(html, /href="\/" class="site-title/);
});
