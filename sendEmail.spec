Name: sendEmail
Version: 1.56
Release: 1%{?dist}
Summary:  An Email program for sending SMTP mail from a command line

License: GPLv2+
URL: http://caspian.dotconf.net/menu/Software/SendEmail/

Source0: http://caspian.dotconf.net/menu/Software/SendEmail/%{name}-v%{version}.tar.gz
Source1: http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
BuildArch: noarch

#Requires: perl

%description
SendEmail is a lightweight, command line SMTP email client. If you
have the need to send email from a command line, this free program is
perfect: simple to use and feature rich. It was designed to be used in
bash scripts, batch files, Perl programs and web sites, but is quite
adaptable and will likely meet your requirements. SendEmail is written
in Perl and is unique in that it requires NO MODULES. It has an
intuitive and flexible set of command-line options, making it very
easy to learn and use.

%prep
%setup -q -n %{name}-v%{version}

%build
# nothing to do

%install
%{__install} -d %{buildroot}%{_bindir}/
%{__install} -m 0755 -p %{name} %{buildroot}%{_bindir}/

%files
%{_bindir}/%{name}
%doc CHANGELOG README TODO

%changelog
* Mon Mar  7 2016 Gerard Ryan <gerard@ryan.lt> - 1.56-1
- Initial spec file creation

