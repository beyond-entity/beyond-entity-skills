# Beyond Entity Skills

BE MCP를 사용하는 AI용 Skill 저장소 초안입니다. Skill 원본은 `skills/beyond-entity/`에 있습니다. 공통 규칙은 `SKILL.md`, 작업별 절차는 `references/`, 도구별 입력·출력 스키마와 Help는 개별 JSON으로 분리했습니다. AI는 필요한 파일만 읽습니다.

이 초안은 `beserv`의 실제 public definition loader와 Guide/Help 구현을 참조합니다. 소스 MCP 버전은 3.2.51이며, 배포된 서버와의 호환성 보장은 아닙니다. 출처·해시는 `skills/beyond-entity/references/source-provenance.json`을 확인하세요. 명시된 outputSchema가 없는 도구는 null로 표시하며 출력 계약을 추정하지 않습니다.

## 설치

`skills/beyond-entity` 폴더 전체를 사용하는 클라이언트의 Skill 경로에 복사하거나 연결하세요. `SKILL.md`만 복사하면 Reference가 누락됩니다. Codex의 사용자 Skill 경로 예시는 `~/.agents/skills/beyond-entity`입니다. 동일 이름의 기존 Skill과 중복 설치하지 않도록 확인하세요. 다른 클라이언트의 경로·재로드 동작은 해당 클라이언트에서 확인해야 합니다.

앱과 AI의 GitHub 직접 다운로드에는 같은 릴리스 ZIP을 사용합니다. 릴리스 자산이 아직 없다면 아래 패키징 명령으로 ZIP을 만들 수 있습니다. 현재 자동 설치·로그인 갱신·서버 읽기 강제는 구현하지 않았습니다. 로컬 Skill 설치는 MCP 연결이나 서버의 Guide 전달 기록을 대신하지 않습니다.

## 참조 갱신과 검증

출력물을 직접 편집하지 않고 도구 계약을 갱신하려면, beserv 의존성이 설치된 Python으로 다음을 실행합니다. 소스를 신뢰할 수 있는 로컬 checkout으로 지정하세요. exporter는 그 소스의 Python 정의 생성 코드를 실행합니다.

```sh
/path/to/beserv/.venv-mcp-build/bin/python scripts/export_reference.py --source /path/to/beserv
python3 scripts/validate.py
python3 scripts/build_package.py --output /path/to/package-output
```

Exporter는 서버 소스나 프로젝트 데이터를 수정하지 않습니다. 현재는 도구 계약과 선택된 Help의 일회 이관 기준선을 소스로부터 재생성하는 단계입니다. 작성한 작업별 Markdown은 신규 저장소에서 관리합니다. 향후 Guide 단일 원본 전환 때에는 서버 Help가 이 저장소의 고정된 콘텐츠 버전을 소비하도록 별도 연결해야 하며, 기존 소스의 Skill/Guide 제거는 아직 수행하지 않았습니다.

검증은 Skill 링크, JSON 참조, 입력·출력 스키마 존재 여부, 도구/Guide 개수, 파일 해시를 확인합니다. 라이브 MCP 호출이나 실제 프로젝트 변경 검증을 대신하지 않습니다. 패키지에는 설치 가능한 Skill 전체와 package manifest가 들어갑니다. ZIP의 SHA-256은 외부 파일로 생성되며, 진위 인증용 서명을 대신하지 않습니다.
