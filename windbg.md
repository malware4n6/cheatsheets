# WinDBG

- [From the SDK](https://developer.microsoft.com/en-us/windows/downloads/windows-sdk/)
- [Version Preview](https://apps.microsoft.com/store/detail/windbg-preview/9PGJGD53TN86)

## Setup

```shell
# cmd as Administrator
setx _NT_SYMBOL_PATH srv*c:\symbols*HTTP://MSDL.MICROSOFT.COM/DOWNLOAD/SYMBOLS
bcdedit /debug on
bcdedit /dbgsettings local
# reboot
```

Shortcut: `ctrl-k` to connect to local debugger
```shell
# in windbg - apply as many times as needed
.symfix c:\symbols
.reload
# if we want the user symbols so that x kernel32!* works
.reload /user
```

## Help

- [windbgcheatsheet](https://sites.google.com/site/taesaza0/etc/windbgcheatsheet?overridemobile=true)
- `.hh`

## Commands

```shell
0n1234
# a number must start with 0n if we want a decimal one

!filetime 1d2b0c063050f28

lkd> .effmach
Effective machine: x64 (AMD64)

lkd> vertarget
Windows 10 Kernel Version 19041 MP (4 procs) Free x64
Product: WinNt, suite: TerminalServer SingleUserTS
Edition build lab: 19041.1.amd64fre.vb_release.191206-1406
Machine Name:
Kernel base = 0xfffff804`3dc00000 PsLoadedModuleList = 0xfffff804`3e82a1d0
Debug session time: Mon Feb 13 13:20:28.180 2023 (UTC - 8:00)
System Uptime: 0 days 2:15:21.601

# list all modules
x *!

x ntdll!*

lkd> x nt!Dbg*
fffff804`3df6f8f0 nt!DbgLoadImageSymbols (void)
fffff804`3df6f944 nt!DbgUnicodeStringToAnsiString (void)
fffff804`3e2b4d74 nt!DbgkCreateThread (void)
fffff804`3e66b920 nt!DbgkInitialize (void)
fffff804`3e217f48 nt!DbgkCopyProcessDebugPort (void)
fffff804`3e2f8b1c nt!DbgkUnMapViewOfSection (void)
fffff804`3e3811e0 nt!DbgkCreateMinimalProcess (void)
fffff804`3e3b6890 nt!DbgkpCreateNotificationEvent (void)
fffff804`3df929d0 nt!DbgEnumerateCallback (void)
fffff804`3e31fa40 nt!DbgkForwardException (void)
fffff804`3e21d9e0 nt!DbgkFlushErrorPort (void)
fffff804`3e2b7100 nt!DbgkMapViewOfSection (void)
fffff804`3e35fd10 nt!DbgkClearProcessDebugObject (void)


# autocomplete is active; use <TAB>
lkd> dx @$curprocess
@$curprocess                 : EngHost.exe [Switch To]
    KernelObject     [Type: _EPROCESS]
    Name             : EngHost.exe
    Id               : 0x1a44
    Handle           : 0xf0f0f0f0
    Threads         
    Modules         
    Environment     
    Devices         
    Io              

lkd> dx @$curprocess.Name
@$curprocess.Name : EngHost.exe
    Length           : 0xb

lkd> dx @$curprocess.Modules
@$curprocess.Modules                
    [0x0]            : ntkrnlmp.exe

lkd> dx @$curprocess.Environment
@$curprocess.Environment                
    EnvironmentBlock [Type: _PEB]

lkd> dx @$curprocess.Environment.EnvironmentBlock
@$curprocess.Environment.EnvironmentBlock                 [Type: _PEB]
    [+0x000] InheritedAddressSpace : 0x0 [Type: unsigned char]
    [+0x001] ReadImageFileExecOptions : 0x0 [Type: unsigned char]
    [+0x002] BeingDebugged    : 0x0 [Type: unsigned char]
    [+0x003] BitField         : 0x14 [Type: unsigned char]
    [+0x003 ( 0: 0)] ImageUsesLargePages : 0x0 [Type: unsigned char]
    [+0x003 ( 1: 1)] IsProtectedProcess : 0x0 [Type: unsigned char]
    [+0x003 ( 2: 2)] IsImageDynamicallyRelocated : 0x1 [Type: unsigned char]
    [+0x003 ( 3: 3)] SkipPatchingUser32Forwarders : 0x0 [Type: unsigned char]
    [+0x003 ( 4: 4)] IsPackagedProcess : 0x1 [Type: unsigned char]
    [+0x003 ( 5: 5)] IsAppContainer   : 0x0 [Type: unsigned char]
    [+0x003 ( 6: 6)] IsProtectedProcessLight : 0x0 [Type: unsigned char]
    [+0x003 ( 7: 7)] IsLongPathAwareProcess : 0x0 [Type: unsigned char]
    [+0x004] Padding0         [Type: unsigned char [4]]
    [+0x008] Mutant           : 0xffffffffffffffff [Type: void *]
    [+0x010] ImageBaseAddress : 0x7ff77d300000 [Type: void *]
    [+0x018] Ldr              : 0x7ffa2e55a4c0 [Type: _PEB_LDR_DATA *]
    [+0x020] ProcessParameters : 0x1aa56a03f70 [Type: _RTL_USER_PROCESS_PARAMETERS *]
    [+0x028] SubSystemData    : 0x0 [Type: void *]

lkd> dx @$curprocess.Environment.EnvironmentBlock.Ldr->InMemoryOrderModuleList
@$curprocess.Environment.EnvironmentBlock.Ldr->InMemoryOrderModuleList                 [Type: _LIST_ENTRY]
    [+0x000] Flink            : 0x1aa56a04cb0 [Type: _LIST_ENTRY *]
    [+0x008] Blink            : 0x1aa5adfd170 [Type: _LIST_ENTRY *]

lkd> dx @$cursession.Processes
@$cursession.Processes                
    [0x0]            : Idle [Switch To]
    [0x4]            : System [Switch To]
    [0x64]           : Registry [Switch To]
    [0x1b8]          : smss.exe [Switch To]
    [0x230]          : csrss.exe [Switch To]
    [0x27c]          : wininit.exe [Switch To]
    [0x288]          : csrss.exe [Switch To]
    [0x2e0]          : winlogon.exe [Switch To]
    [0x310]          : services.exe [Switch To]

lkd> dx @$cursession.Processes.Select(p => p.Name) 
@$cursession.Processes.Select(p => p.Name)                 
    [0x0]            : Idle
    [0x4]            : System
    [0x64]           : Registry
    [0x1b8]          : smss.exe
    [0x230]          : csrss.exe
    [0x27c]          : wininit.exe
    [0x288]          : csrss.exe
    [0x2e0]          : winlogon.exe
    [0x310]          : services.exe


lkd> dx @$cursession.Processes.Select(p => new { Name = p.Name, Module_count = p.Modules.Count() })
@$cursession.Processes.Select(p => new { Name = p.Name, Module_count = p.Modules.Count() })                
    [0x0]           
    [0x4]           
    [0x64]          
    [0x1b8]  


lkd> dx -r1 @$cursession.Processes.Select(p => new { Name = p.Name, Module_count = p.Modules.Count() })[4]
@$cursession.Processes.Select(p => new { Name = p.Name, Module_count = p.Modules.Count() })[4]                
    Name             : System
    Module_count     : 0x1

dx -r1 @$cursession.Processes.First()

lkd> dx (nt!_EPROCESS*)0xffffdd06408c0140
(nt!_EPROCESS*)0xffffdd06408c0140                 : 0xffffdd06408c0140 [Type: _EPROCESS *]
    [+0x000] Pcb              [Type: _KPROCESS]
    [+0x438] ProcessLock      [Type: _EX_PUSH_LOCK]
    [+0x440] UniqueProcessId  : 0x900 [Type: void *]
    [+0x448] ActiveProcessLinks [Type: _LIST_ENTRY]
    [+0x458] RundownProtect   [Type: _EX_RUNDOWN_REF]
    [+0x460] Flags2           : 0xd000 [Type: unsigned long]
    [+0x460 ( 0: 0)] JobNotReallyActive : 0x0 [Type: unsigned long]
    [+0x460 ( 1: 1)] AccountingFolded : 0x0 [Type: unsigned long]
    [+0x460 ( 2: 2)] NewProcessReported : 0x0 [Type: unsigned long]
    [+0x460 ( 3: 3)] ExitProcessReported : 0x0 [Type: unsigned long]
    [+0x460 ( 4: 4)] ReportCommitChanges : 0x0 [Type: unsigned long]
    [+0x460 ( 5: 5)] LastReportMemory : 0x0 [Type: unsigned long]
    [+0x460 ( 6: 6)] ForceWakeCharge  : 0x0 [Type: unsigned long]
    [+0x460 ( 7: 7)] CrossSessionCreate : 0x0 [Type: unsigned long]
    [+0x460 ( 8: 8)] NeedsHandleRundown : 0x0 [Type: unsigned long]
    [+0x460 ( 9: 9)] RefTraceEnabled  : 0x0 [Type: unsigned long]
    [+0x460 (10:10)] PicoCreated      : 0x0 [Type: unsigned long]
    [+0x460 (11:11)] EmptyJobEvaluated : 0x0 [Type: unsigned long]
    [+0x460 (14:12)] DefaultPagePriority : 0x5 [Type: unsigned long]
    [+0x460 (15:15)] PrimaryTokenFrozen : 0x1 [Type: unsigned long]
    [+0x460 (16:16)] ProcessVerifierTarget : 0x0 [Type: unsigned long]
    [+0x460 (17:17)] RestrictSetThreadContext : 0x0 [Type: unsigned long]
    [+0x460 (18:18)] AffinityPermanent : 0x0 [Type: unsigned long]
    [+0x460 (19:19)] AffinityUpdateEnable : 0x0 [Type: unsigned long]
    [+0x460 (20:20)] PropagateNode    : 0x0 [Type: unsigned long]
    [+0x460 (21:21)] ExplicitAffinity : 0x0 [Type: unsigned long]
    [+0x460 (23:22)] ProcessExecutionState : 0x0 [Type: unsigned long]
    [+0x460 (24:24)] EnableReadVmLogging : 0x0 [Type: unsigned long]
    [+0x460 (25:25)] EnableWriteVmLogging : 0x0 [Type: unsigned long]
    [+0x460 (26:26)] FatalAccessTerminationRequested : 0x0 [Type: unsigned long]
    [+0x460 (27:27)] DisableSystemAllowedCpuSet : 0x0 [Type: unsigned long]
    [+0x460 (29:28)] ProcessStateChangeRequest : 0x0 [Type: unsigned long]
    [+0x460 (30:30)] ProcessStateChangeInProgress : 0x0 [Type: unsigned long]
    [+0x460 (31:31)] InPrivate        : 0x0 [Type: unsigned long]
    [+0x464] Flags            : 0x14440c01 [Type: unsigned long]
    [+0x464 ( 0: 0)] CreateReported   : 0x1 [Type: unsigned long]
    [+0x464 ( 1: 1)] NoDebugInherit   : 0x0 [Type: unsigned long]
    [+0x464 ( 2: 2)] ProcessExiting   : 0x0 [Type: unsigned long]
    [+0x464 ( 3: 3)] ProcessDelete    : 0x0 [Type: unsigned long]
    [+0x464 ( 4: 4)] ManageExecutableMemoryWrites : 0x0 [Type: unsigned long]
    [+0x464 ( 5: 5)] VmDeleted        : 0x0 [Type: unsigned long]
    [+0x464 ( 6: 6)] OutswapEnabled   : 0x0 [Type: unsigned long]
    [+0x464 ( 7: 7)] Outswapped       : 0x0 [Type: unsigned long]
    [+0x464 ( 8: 8)] FailFastOnCommitFail : 0x0 [Type: unsigned long]
    [+0x464 ( 9: 9)] Wow64VaSpace4Gb  : 0x0 [Type: unsigned long]
    [+0x464 (11:10)] AddressSpaceInitialized : 0x3 [Type: unsigned long]
    [+0x464 (12:12)] SetTimerResolution : 0x0 [Type: unsigned long]
    [+0x464 (13:13)] BreakOnTermination : 0x0 [Type: unsigned long]
    [+0x464 (14:14)] DeprioritizeViews : 0x0 [Type: unsigned long]
    [+0x464 (15:15)] WriteWatch       : 0x0 [Type: unsigned long]
    [+0x464 (16:16)] ProcessInSession : 0x0 [Type: unsigned long]
    [+0x464 (17:17)] OverrideAddressSpace : 0x0 [Type: unsigned long]
    [+0x464 (18:18)] HasAddressSpace  : 0x1 [Type: unsigned long]
    [+0x464 (19:19)] LaunchPrefetched : 0x0 [Type: unsigned long]
    [+0x464 (20:20)] Background       : 0x0 [Type: unsigned long]
    [+0x464 (21:21)] VmTopDown        : 0x0 [Type: unsigned long]
    [+0x464 (22:22)] ImageNotifyDone  : 0x1 [Type: unsigned long]
    [+0x464 (23:23)] PdeUpdateNeeded  : 0x0 [Type: unsigned long]
    [+0x464 (24:24)] VdmAllowed       : 0x0 [Type: unsigned long]
    [+0x464 (25:25)] ProcessRundown   : 0x0 [Type: unsigned long]
    [+0x464 (26:26)] ProcessInserted  : 0x1 [Type: unsigned long]
    [+0x464 (29:27)] DefaultIoPriority : 0x2 [Type: unsigned long]
    [+0x464 (30:30)] ProcessSelfDelete : 0x0 [Type: unsigned long]
    [+0x464 (31:31)] SetTimerResolutionLink : 0x0 [Type: unsigned long]
    [+0x468] CreateTime       : {133207887101165497} [Type: _LARGE_INTEGER]
    [+0x470] ProcessQuotaUsage [Type: unsigned __int64 [2]]
    [+0x480] ProcessQuotaPeak [Type: unsigned __int64 [2]]
    [+0x490] PeakVirtualSize  : 0xc960000 [Type: unsigned __int64]
    [+0x498] VirtualSize      : 0xc960000 [Type: unsigned __int64]
    [+0x4a0] SessionProcessLinks [Type: _LIST_ENTRY]
    [+0x4b0] ExceptionPortData : 0x0 [Type: void *]
    [+0x4b0] ExceptionPortValue : 0x0 [Type: unsigned __int64]
    [+0x4b0 ( 2: 0)] ExceptionPortState : 0x0 [Type: unsigned __int64]
    [+0x4b8] Token            [Type: _EX_FAST_REF]

```

## Javascript

```javascript
"use strict";

host.diagnostics.debugLog("Hello froms script!\n");

function initializeScript() {
    return [new host.apiVersionSupport(1, 7)];
}

function log(data) {
    host.diagnostics.debugLog(data + "\n");
}

function invokeScript() {
    log("foo")
    log(host.currentProcess)
}

function readMemAt(addr, length) {
    return host.memory.readMemoryValues(addr, length);
}
```

```shell
# executes "root" script and initializeScript()
.scriptload c:\scripts.hello.js
# also calls invokeScript()
.scriptrun c:\scripts.hello.js
.scriptunload c:\scripts.hello.js
```