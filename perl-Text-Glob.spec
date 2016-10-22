%{?scl:%scl_package perl-Text-Glob}

Name: 		%{?scl_prefix}perl-Text-Glob
Version: 	0.09
Release: 	17%{?dist}
Summary: 	Perl module to match globbing patterns against text
License: 	GPL+ or Artistic
Group: 		Development/Libraries
URL: 		http://search.cpan.org/dist/Text-Glob/
Source0: 	http://www.cpan.org/authors/id/R/RC/RCLAMP/Text-Glob-%{version}.tar.gz

BuildArch: noarch
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(Test::More)
Requires:  %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))

%description
Text::Glob implements glob(3) style matching that can be used to match
against text, rather than fetching names from a file-system.  If you
want to do full file globbing use the File::Glob module instead.

%prep
%setup -q -n Text-Glob-%{version}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=$RPM_BUILD_ROOT%{?scl:'}
chmod -R u+w $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc Changes
%{perl_vendorlib}/Text
%{_mandir}/man3/*

%changelog
* Tue Jul 19 2016 Petr Pisar <ppisar@redhat.com> - 0.09-17
- SCL

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-16
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 30 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.09-14
- Modernize spec.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-12
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-11
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.09-8
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Aug 10 2012 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-6
- Update BRs and remove %%defattr.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 0.09-4
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.09-2
- Perl mass rebuild

* Wed Mar 02 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.09-1
- Upstream update.
- Spec cleanup.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 23 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.08-10
- 661697 rebuild for fixing problems with vendorach/lib

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.08-9
- Mass rebuild with perl-5.12.0

* Thu Feb 25 2010 Marcela Mašláňová <mmaslano@redhat.com> - 0.08-8
- add readme

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.08-7
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.08-4
- Rebuild for perl 5.10 (again)

* Fri Jan 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.08-3
- rebuild for new perl

* Sat Aug 18 2007 Ralf Corsépius <rc040203@freenet.de> - 0.08-2
- Update license tag.

* Tue May 08 2007 Ralf Corsépius <rc040203@freenet.de> - 0.08-1
- Upstream update.

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 0.07-2
- Mass rebuild.

* Thu Jul 20 2006 Ralf Corsépius <rc040203@freenet.de> - 0.07-1
- Upstream update.

* Tue Feb 28 2006 Ralf Corsépius <rc040203@freenet.de> - 0.06-4
- Rebuild for perl-5.8.8.

* Wed Aug 10 2005 Ralf Corsepius <ralf@links2linux.de> - 0.06-3
- Spec cleanup.

* Wed Aug 10 2005 Ralf Corsepius <ralf@links2linux.de> - 0.06-2
- FE resubmission.

* Fri Jul 01 2005 Ralf Corsepius <ralf@links2linux.de> - 0.06-1
- FE submission.
