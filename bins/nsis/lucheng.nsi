!include "MUI2.nsh"

Name "Lucheng Test"
OutFile "Lucheng.exe"

ShowInstDetails show

!define MUI_ICON ".\icon\favicon.ico"

InstallDir "$LOCALAPPDATA\lucheng Test"

;Pages
!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_LICENSE "${NSISDIR}\Docs\Modern UI\License.txt"
!insertmacro MUI_PAGE_COMPONENTS
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_UNPAGE_WELCOME
!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES
!insertmacro MUI_UNPAGE_FINISH

;Languages
!insertmacro MUI_LANGUAGE "English"


;Installer Sections

Section "lucheng1" SecDump

  SetOutPath "$INSTDIR"

  ;ADD YOUR OWN FILES HERE...
  Messagebox MB_OK|MB_ICONINFORMATION \
	"This is a sample that shows how to use line breaks for larger commands in NSIS scripts"

  ;Create uninstaller
  WriteUninstaller "$INSTDIR\Uninstall.exe"

SectionEnd

Section "lucheng2" SecDump2

  SetOutPath "$INSTDIR"

  ;ADD YOUR OWN FILES HERE...
  File *.exe

SectionEnd

Section "test"
  Messagebox MB_OK|MB_ICONINFORMATION "test execute"
  nsExec::ExecToStack '"${NSISDIR}\makensis.exe" /VERSION'
  Pop $0
  Pop $1
  DetailPrint "       Return value: $0"  
SectionEnd

LangString DESC_SecDump ${LANG_ENGLISH} "A test lucheng section."
LangString DESC_SecDump2 ${LANG_ENGLISH} "A test lucheng2 section."

;Assign language strings to sections
!insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
!insertmacro MUI_DESCRIPTION_TEXT ${SecDump} $(DESC_SecDump)
!insertmacro MUI_DESCRIPTION_TEXT ${SecDump2} $(DESC_SecDump2)
!insertmacro MUI_FUNCTION_DESCRIPTION_END

Section "Uninstall"
Delete "$INSTDIR\*.exe"
Delete "$INSTDIR\Uninstall.exe"
RMDir "$INSTDIR"
SectionEnd


Function .onInit
  ; MessageBox MB_YESNO "This will install My Program. Do you wish to continue?" IDYES gogogo
    ; Abort
  ; gogogo:



FunctionEnd


