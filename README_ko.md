# Beyond Entity Skills

[English](README.md) · **한국어**

BE MCP를 사용하는 AI용 Skill 저장소 초안입니다. Skill 원본은 `skills/beyond-entity/`에 있습니다. 공통 규칙은 `SKILL.md`, 작업별 절차는 `references/`, 도구별 입력·출력 스키마와 Help는 개별 JSON으로 분리했습니다. AI는 필요한 파일만 읽습니다.

이 초안은 `beserv`의 실제 public definition loader와 Guide/Help 구현을 참조합니다. 소스 MCP 버전은 3.2.53이며, 배포된 서버와의 호환성 보장은 아닙니다. 출처·해시는 `skills/beyond-entity/references/source-provenance.json`을 확인하세요. 명시된 outputSchema가 없는 도구는 null로 표시하며 출력 계약을 추정하지 않습니다.

## Transformation 이름

이름만 바꿀 때는 `beyond_rename_transformation`을 사용합니다. 기존 Transformation의 ID, 원본 SQL, 처리 순서, 항목, 리니지를 보존합니다. 먼저 현재 Transformation을 읽고 동작과 목적을 나타내는 짧은 이름을 지정한 다음 저장 결과를 확인하세요. 자세한 절차는 [Transformation 지침](skills/beyond-entity/references/transformations.md)을 참고하세요.

## 설치

[공식 Releases](https://github.com/beyond-entity/beyond-entity-skills/releases)에서 안정 릴리스의 `beyond-entity-skill-<version>.zip`과 대응하는 `.zip.sha256` 파일을 받으세요. 압축을 풀기 전에 ZIP의 SHA-256, 내부 package manifest, 개별 파일 해시를 검증합니다.

설치에 사용할 MCP 연결에서 `beyond_get_mcp_version`을 호출하세요. Manifest의 `compatibility.validated_runtime_versions`에 해당 버전이 정확히 포함돼 있어야 합니다. 소스 기준 버전만으로 호환성을 판단하지 않습니다.

압축 안의 `beyond-entity` 폴더 전체를 클라이언트가 지원하는 Skill 경로에 설치하세요. `SKILL.md`만 복사하면 Reference가 누락됩니다. Codex 사용자 Skill 경로 예시는 `~/.agents/skills/beyond-entity`, Claude Code 개인 Skill 경로는 `~/.claude/skills/beyond-entity`입니다. 기존 설치와 사용자 변경을 보존하고 중복 설치를 피하세요. 클라이언트의 Skill 탐색에 필요하면 재로드하거나 새 세션을 시작합니다.

소스 checkout에서 설치할 폴더는 `skills/beyond-entity/`입니다. 검증된 런타임 목록이 없는 로컬 패키지는 검사 용도로 사용할 수 있으며, 활성화 전에는 런타임 호환성을 검증해야 합니다.

Skill 설치는 MCP 연결이나 서버의 Guide 전달 확인을 대신하지 않습니다.

## 참조 갱신과 검증

출력물을 직접 편집하지 않고 도구 계약을 갱신하려면, beserv 의존성이 설치된 Python으로 다음을 실행합니다. 소스를 신뢰할 수 있는 로컬 checkout으로 지정하세요. exporter는 그 소스의 Python 정의 생성 코드를 실행합니다.

```sh
/path/to/beserv/.venv-mcp-build/bin/python scripts/export_reference.py --source /path/to/beserv
python3 scripts/validate.py
python3 scripts/build_package.py --output /path/to/package-output
```

Exporter는 서버 소스나 프로젝트 데이터를 수정하지 않습니다. 현재는 도구 계약과 선택된 Help의 일회 이관 기준선을 소스로부터 재생성하는 단계입니다. 작성한 작업별 Markdown은 신규 저장소에서 관리합니다. 향후 Guide 단일 원본 전환 때에는 서버 Help가 이 저장소의 고정된 콘텐츠 버전을 소비하도록 별도 연결해야 하며, 기존 소스의 Skill/Guide 제거는 아직 수행하지 않았습니다.

검증은 Skill 링크, JSON 참조, 입력·출력 스키마 존재 여부, 도구/Guide 개수, 파일 해시를 확인합니다. 라이브 MCP 호출이나 실제 프로젝트 변경 검증을 대신하지 않습니다. 패키지에는 설치 가능한 Skill 전체와 package manifest가 들어갑니다. ZIP의 SHA-256은 외부 파일로 생성되며, 진위 인증용 서명을 대신하지 않습니다.

런타임 검증을 통과한 릴리스 후보는 검증한 정확한 버전을 기록하여 패키징합니다.

```sh
python3 scripts/build_package.py --output /path/to/package-output --validated-runtime-version 3.2.53
```

이 옵션은 관리자가 수행한 검증을 기록합니다. 런타임 테스트를 실행하거나 `source_mcp_version`에서 호환성을 추정하지 않습니다. 옵션을 생략하면 검증된 런타임 목록은 비어 있습니다.
