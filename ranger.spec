Summary:	A simple, vim-like file manager
Summary(hu.UTF-8):	Egyszerű, vim-szerű fájlkezelő
Name:		ranger
Version:	1.5.2
Release:	0.1
License:	GPL v3
Group:		Applications/Shells
Source0:	http://nongnu.org/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	75b1e15b50ecced0a337ae30741daa3b
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/%{name}
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/ranger-%{version}-py2.7.egg-info
%endif
%{py_sitescriptdir}/ranger
%{_mandir}/man1/ranger*
