Summary:	A simple, vim-like file manager
Summary(hu.UTF-8):	Egyszerű, vim-szerű fájlkezelő
Name:		ranger
Version:	1.9.2
Release:	1
License:	GPL v3
Group:		Applications/Shells
Source0:	https://ranger.github.io/%{name}-%{version}.tar.gz
# Source0-md5:	08970e4343ac0457a60befa1ec97f62b
URL:		https://ranger.github.io/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple, vim-like file manager.

%description -l hu.UTF-8
Egyszerű, vim-szerű fájlkezelő.

%prep
%setup -q

%build
%{__make} compile

%install
rm -rf $RPM_BUILD_ROOT

%py_install
%py_postclean

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

cp -p examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

rm -r $RPM_BUILD_ROOT%{_docdir}/ranger

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG.md HACKING.md README.md doc/colorschemes.md doc/config doc/tools
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/rifle
%{_desktopdir}/ranger.desktop
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/ranger_fm-%{version}-py2.7.egg-info
%endif
%dir %{py_sitescriptdir}/ranger
%{py_sitescriptdir}/ranger/api
%{py_sitescriptdir}/ranger/colorschemes
%{py_sitescriptdir}/ranger/config
%{py_sitescriptdir}/ranger/container
%{py_sitescriptdir}/ranger/core
%dir %{py_sitescriptdir}/ranger/data
%{py_sitescriptdir}/ranger/data/mime.types
%attr(755,root,root) %{py_sitescriptdir}/ranger/data/scope.sh
%{py_sitescriptdir}/ranger/ext
%{py_sitescriptdir}/ranger/gui
%{py_sitescriptdir}/ranger/*.py[co]
%{_mandir}/man1/ranger.1*
%{_mandir}/man1/rifle.1*
%{_examplesdir}/%{name}-%{version}
