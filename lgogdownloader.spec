Name:		lgogdownloader
Version:	3.18
Release:	2
Summary:	GOG.com download client
Group:          Games/Internet
License:	WTFPL
URL:		https://github.com/Sude-/lgogdownloader
Source0:	https://github.com/Sude-/lgogdownloader/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:	cmake
BuildOption:	-DUSE_QT_GUI=ON
BuildRequires:  qmake-qt6
BuildRequires:	help2man
BuildRequires:	binutils
BuildRequires:  %{_lib}htmlcxx3
BuildRequires:  %{_lib}cssparser0
BuildRequires:  %{_lib}cssparser-devel
BuildRequires:	pkgconfig(htmlcxx)
BuildRequires:	pkgconfig(jsoncpp)
BuildRequires:	pkgconfig(libcrypto)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(tinyxml2)
BuildRequires:  pkgconfig(tidy)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	boost-devel
BuildRequires:	rhash-devel
BuildRequires:	pkgconfig(Qt6WebEngineCore)
BuildRequires:	pkgconfig(Qt6WebEngineWidgets)
BuildRequires:	pkgconfig(Qt6Widgets)

%description
LGOGDownloader is an unofficial GOG.com downloader for Linux users. It uses the
same API as the official GOG Galaxy.

%conf -p
export LDFLAGS="%{optflags} -lcurl"

%files
%license COPYING
%{_bindir}/lgogdownloader
%{_mandir}/man1/lgogdownloader.1.*
