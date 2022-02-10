%define		kodi_ver	19
%define		next_kodi_ver	%(echo $((%{kodi_ver}+1)))
%define		codename	Matrix
%define		addon		video.eurosporton

Summary:	Proof-of-concept Kodi plugin for Eurosport Player
Name:		kodi-addon-video-eurosporton
Version:	0.2.3
Release:	1
License:	GPL v2+
Group:		Applications/Multimedia
Source0:	https://github.com/sterd71/plugin.video.eurosporton/archive/v%{version}-k%{kodi_ver}-Oly/%{version}-%{codename}.tar.gz
# Source0-md5:	577eee3df60421d8ef3266fde988f126
URL:		https://github.com/sterd71/plugin.video.eurosporton/
Requires:	kodi >= %{kodi_ver}
Requires:	kodi < %{next_kodi_ver}
Suggests:	kodi-addon-inputstream-adaptive
Suggests:	kodi-addon-inputstream-ffmpegdirect
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Proof-of-concept Kodi plugin for Eurosport Player.

%prep
%setup -q -n plugin.video.eurosporton-%{version}-k%{kodi_ver}-Oly

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/kodi/addons/%{addon}
cp -rp addon.xml changelog.txt main.py resources $RPM_BUILD_ROOT%{_datadir}/kodi/addons/%{addon}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%dir %{_datadir}/kodi/addons/%{addon}
%{_datadir}/kodi/addons/%{addon}/addon.xml
%{_datadir}/kodi/addons/%{addon}/changelog.txt
%{_datadir}/kodi/addons/%{addon}/main.py
%{_datadir}/kodi/addons/%{addon}/resources
