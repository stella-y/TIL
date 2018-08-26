## JQ - command line json parser
* command line 으로 json 다룰 수 있게 해줌
* download
```bash
sudo apt-get install jq
```
* 기본 명령
	jq + 필터
* 특정 내용 조회
```bash
cat example.json | jq .production.version
```
	jq 하위 항목 조회함
* shell 에서 변수로 저장
```bash
test_var=$(cat example.json | jq .production.version)
echo $test_var
```

* 첫번째 요소 가져오기
```bash
curl 'https://api.github.com/repos/stedolan/jq/commits?per_page=5' | jq '.[0]'
```

* 각 요소 parsing
- cmd
```bash
jq '.[0] | {message: .commit.message, name: .commit.committer.name}'
```
- result
```json
{
  "message": "Merge pull request #162 from stedolan/utf8-fixes\n\nUtf8 fixes. Closes #161",
  "name": "Stephen Dolan"
}
```

-cmd
```bash
jq '.[] | {message: .commit.message, name: .commit.committer.name}'
```
-result
```json
{
  "message": "Merge pull request #162 from stedolan/utf8-fixes\n\nUtf8 fixes. Closes #161",
  "name": "Stephen Dolan"
}
{
  "message": "Reject all overlong UTF8 sequences.",
  "name": "Stephen Dolan"
}
{
  "message": "Fix various UTF8 parsing bugs.\n\nIn particular, parse bad UTF8 by replacing the broken bits with U+FFFD\nand resychronise correctly after broken sequences.",
  "name": "Stephen Dolan"
}
{
  "message": "Fix example in manual for `floor`. See #155.",
  "name": "Stephen Dolan"
}
{
  "message": "Document floor",
  "name": "Nicolas Williams"
}
```

- cmd
```bash
jq '[.[] | {message: .commit.message, name: .commit.committer.name}]'
```
- result
```json
[
  {
    "message": "Merge pull request #163 from stedolan/utf8-fixes\n\nUtf8 fixes. Closes #161",
    "name": "Stephen Dolan"
  },
  {
    "message": "Reject all overlong UTF8 sequences.",
    "name": "Stephen Dolan"
  },
  {
    "message": "Fix various UTF8 parsing bugs.\n\nIn particular, parse bad UTF8 by replacing the broken bits with U+FFFD\nand resychronise correctly after broken sequences.",
    "name": "Stephen Dolan"
  },
  {
    "message": "Fix example in manual for `floor`. See #155.",
    "name": "Stephen Dolan"
  },
  {
    "message": "Document floor",
    "name": "Nicolas Williams"
  }
]
```

example
```json
"parents": [
  {
    "sha": "54b9c9bdb225af5d886466d72f47eafc51acb4f7",
    "url": "https://api.github.com/repos/stedolan/jq/commits/54b9c9bdb225af5d886466d72f47eafc51acb4f7",
    "html_url": "https://github.com/stedolan/jq/commit/54b9c9bdb225af5d886466d72f47eafc51acb4f7"
  },
  {
    "sha": "8b1b503609c161fea4b003a7179b3fbb2dd4345a",
    "url": "https://api.github.com/repos/stedolan/jq/commits/8b1b503609c161fea4b003a7179b3fbb2dd4345a",
    "html_url": "https://github.com/stedolan/jq/commit/8b1b503609c161fea4b003a7179b3fbb2dd4345a"
  }
]
```
- cmd
```bash
jq '[.[] | {message: .commit.message, name: .commit.committer.name, parents: [.parents[].html_url]}]'
```
- result
```json
[
  {
    "message": "Merge pull request #162 from stedolan/utf8-fixes\n\nUtf8 fixes. Closes #161",
    "name": "Stephen Dolan",
    "parents": [
      "https://github.com/stedolan/jq/commit/54b9c9bdb225af5d886466d72f47eafc51acb4f7",
      "https://github.com/stedolan/jq/commit/8b1b503609c161fea4b003a7179b3fbb2dd4345a"
    ]
  },
  {
    "message": "Reject all overlong UTF8 sequences.",
    "name": "Stephen Dolan",
    "parents": [
      "https://github.com/stedolan/jq/commit/ff48bd6ec538b01d1057be8e93b94eef6914e9ef"
    ]
  },
  {
    "message": "Fix various UTF8 parsing bugs.\n\nIn particular, parse bad UTF8 by replacing the broken bits with U+FFFD\nand resychronise correctly after broken sequences.",
    "name": "Stephen Dolan",
    "parents": [
      "https://github.com/stedolan/jq/commit/54b9c9bdb225af5d886466d72f47eafc51acb4f7"
    ]
  },
  {
    "message": "Fix example in manual for `floor`. See #155.",
    "name": "Stephen Dolan",
    "parents": [
      "https://github.com/stedolan/jq/commit/3dcdc582ea993afea3f5503a78a77675967ecdfa"
    ]
  },
  {
    "message": "Document floor",
    "name": "Nicolas Williams",
    "parents": [
      "https://github.com/stedolan/jq/commit/7c4171d414f647ab08bcd20c76a4d8ed68d9c602"
    ]
  }
]
```