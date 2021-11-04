Name:		lgogdownloader
Version:	3.8
Release:	2%{?dist}
Summary:	GOG.com download client

License:	WTFPL
URL:		https://github.com/Sude-/lgogdownloader
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	help2man
BuildRequires:	binutils
BuildRequires:	pkgconfig(htmlcxx)
BuildRequires:	pkgconfig(jsoncpp)
BuildRequires:	pkgconfig(libcrypto)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(tinyxml2)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	boost-devel
BuildRequires:	rhash-devel
%ifarch %{qt5_qtwebengine_arches}
BuildRequires:	pkgconfig(Qt5WebEngine)
%endif

%description
LGOGDownloader is an unofficial GOG.com downloader for Linux users. It uses the
same API as the official GOG Galaxy.

%prep
%autosetup

%build
%ifarch %{qt5_qtwebengine_arches}
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_TYPE=Release -DUSE_QT_GUI=ON .
%else
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_TYPE=Release -DUSE_QT_GUI=OFF .
%endif
%cmake_build

%install
%cmake_install

%files
%license COPYING
%{_bindir}/lgogdownloader
%{_mandir}/man1/lgogdownloader.1.*

%changelog
* Wed Nov 03 2021 BjĂśrn Esser <besser82@fedoraproject.org> - 3.8-2
- Rebuild (jsoncpp)

* Mon Sep 27 2021 Benjamin Lowry <ben@ben.gmbh> - 3.8-1
- lgogdownloader 3.8

* Fri Aug 06 2021 Jonathan Wakely <jwakely@redhat.com> - 3.7-9
- Rebuilt for Boost 1.76

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 3.7-6
- Rebuilt for Boost 1.75

* Sat Aug 01 2020 Benjamin Lowry <ben@ben.gmbh> - 3.7-5
- Update to new cmake macros, fix build error

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Benjamin Lowry <ben@ben.gmbh> 3.7-2
- Change source0 URL
- Replace /usr with _prefix macro
- Glob extension of manpage file
* Thu Jun 18 2020 Benjamin Lowry <ben@ben.gmbh> 3.7-1
- Initial Fedora package
