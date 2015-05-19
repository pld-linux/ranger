Summary:	A simple, vim-like file manager
Summary(hu.UTF-8):	Egyszerű, vim-szerű fájlkezelő
Name:		ranger
Version:	1.7.1
Release:	1
License:	GPL v3
Group:		Applications/Shells
Source0:	http://nongnu.org/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	ec64bc12d3edfd784b1d67023fdf21fc
URL:		http://savannah.nongnu.org/projects/ranger/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple, vim-like file manager.

%description -l hu.UTF-8
Egyszerű, vim-szerű fájlkezelő.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

cp -p examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

rm -r $RPM_BUILD_ROOT%{_docdir}/ranger

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG HACKING.md README.md doc/colorschemes.txt doc/config doc/tools
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/rifle
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/ranger-%{version}-py2.7.egg-info
%endif
%{py_sitescriptdir}/ranger
%{_mandir}/man1/ranger.1*
%{_mandir}/man1/rifle.1*
%{_examplesdir}/%{name}-%{version}
