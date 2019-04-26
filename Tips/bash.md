## sed
* (=stream editor)
* 텍스트 변환 유틸
* 줄단위(\n)처리를 함
* 줄단위 처리가 기본이지만 메모리를 이용해 여러줄 처리도 가능

### 줄 치환
* substitute (s/pattern/replace/)
	* 해당 패턴을 포함한 line remove
		```
		sed 's/pattern/d'
		```
	* 해당 패턴만 삭제
		```
		sed 's/\[//g'
		sed 's/\[//g' $embedding_path/before_sed.txt > $embedding_path/sed1.txt
		```
* i option 주면 바꾼 상태로 파일 저장(tmp 파일 생성 후 동일 이름으로 다시 복사하는 방식)
```sh
sed -i "s/변경전문자열/변경후문자열/g" [파일]
```

### 줄 삭제
```sh
$ echo -e "aaa\nbbb\nccc\nddd" | sed "2d"
aaa
ccc
ddd
```
### 특정파일 특정 줄에만 접근
```bash
sed -n 56063p entertain_3mon_like_title.csv
```
56063번째줄만 읽기


## awk
https://zetawiki.com/wiki/%EB%A6%AC%EB%88%85%EC%8A%A4_sed
https://zetawiki.com/wiki/%EB%A6%AC%EB%88%85%EC%8A%A4_awk

## 서버 사양 확인
### cpu 확인
* cpu 정보 확인
	* processor 별로 model name 등 cpu 정보
```bash
cat /proc/cpuinfo
```
```bash
processor	: 0 # processor 갯수 grep -c processor /proc/cpuinfo
vendor_id	: GenuineIntel
cpu family	: 6
model		: 63
model name	: Intel(R) Xeon(R) CPU E5-2620 v3 @ 2.40GHz # cpu 모델명
stepping	: 2
microcode	: 0x3d
cpu MHz		: 2397.407
cache size	: 15360 KB
physical id	: 0
siblings	: 12
core id		: 0
cpu cores	: 6
apicid		: 0
initial apicid	: 0
fpu		: yes
fpu_exception	: yes
cpuid level	: 15
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid dca sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm epb intel_ppin ssbd ibrs ibpb stibp tpr_shadow vnmi flexpriority ept vpid fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid cqm xsaveopt cqm_llc cqm_occup_llc dtherm ida arat pln pts spec_ctrl intel_stibp
bogomips	: 4794.81
clflush size	: 64
cache_alignment	: 64
address sizes	: 46 bits physical, 48 bits virtual
power management:
```
* 위에서 processor 갯수는, hyperthreading 때문에 실제 코어수의 2배로 인식됨(싱글코어는 코어 두개, 듀얼 코어는 네개로 인식됨)
* 물리 cpu 갯수, cpu 당 물리 코어 수
```bash
grep "physical id" /proc/cpuinfo | sort -u | wc -l #물리 cpu 갯수
grep "cpu cores" /proc/cpuinfo | tail -1 # cpu 당 물리 코어 수

```

### RAM 확인
```bash
cat /proc/meminfo | grep MemTotal
```

### storage 확인
```bash
df -h
```
* 참고 : https://m.blog.naver.com/PostView.nhn?blogId=skemfl57&logNo=220656881773&proxyReferer=https%3A%2F%2Fwww.google.com%2F







