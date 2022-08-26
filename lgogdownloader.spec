Name:		lgogdownloader
Version:	3.9
Release:	2
Summary:	GOG.com download client
Group:          Games/Internet
License:	WTFPL
URL:		https://github.com/Sude-/lgogdownloader
Source0:	https://github.com/Sude-/lgogdownloader/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:  qmake5
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
BuildRequires:	pkgconfig(zlib)
BuildRequires:	boost-devel
BuildRequires:	rhash-devel
BuildRequires:	pkgconfig(Qt5WebEngine)
BuildRequires:  pkgconfig(Qt5WebEngineWidgets)
BuildRequires:  pkgconfig(Qt5Widgets)

%description
LGOGDownloader is an unofficial GOG.com downloader for Linux users. It uses the
same API as the official GOG Galaxy.

%prep
%autosetup -p1

%build

%cmake  \
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DCMAKE_BUILD_TYPE=Release \
        -DUSE_QT_GUI=ON
%make_build

%install
%make_install -C build

%files
%license COPYING
%{_bindir}/lgogdownloader
%{_mandir}/man1/lgogdownloader.1.*
